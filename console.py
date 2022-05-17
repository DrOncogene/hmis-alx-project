#!/usr/bin/python3
"""the console module to control the models"""
import cmd
import readline
import sys
import json
import re
from models import storage
from models.doctor import Doctor
from models.nurse import Nurse
from models.pharmacist import Pharmacist
from models.record import RecordOfficer
from models.admin import Admin
from models.notes.consult import Consultation
from models.notes.prescription import Prescription
from models.notes.vitals import VitalSign
from models.notes.nursesnote import NursesNote
from models.drug import Drug

class HMIS(cmd.Cmd):
    """class the defines the console object"""
    prompt = "(hmis) "
    _classes = {
        "Doctor": Doctor,
        "Nurse": Nurse,
        "Pharmacist": Pharmacist,
        "RecordOfficer": RecordOfficer,
        "Admin": Admin,
        "Consultation": Consultation,
        "Prescription": Prescription,
        "VitalSign": VitalSign,
        "NursesNote": NursesNote,
        "Drug": Drug
    }

    def do_EOF(self, arg: str) -> None:
        """Exits the interpreter when crtl+D is entered.
        USAGE: EOF\n"""
        sys.exit(0)

    def do_quit(self, arg: str) -> None:
        """Quit command to exit the program\n"""
        sys.exit(0)

    def emptyline(self):
        return

    def default(self, arg: str) -> None:
        pattern = re.compile(r'(\w+)\.(\w+)\(([\S ]*)\)')
        res = pattern.findall(arg)
        if len(res) < 1 or len(res[0]) < 3:
            super().default(arg)
            return
        class_name = res[0][0]
        command = res[0][1]
        args = res[0][2]
        if command == "all":
            self.onecmd(f"{command} {class_name}")
            return
        elif command == "count":
            count = self.do_all(f"{class_name}", count=True)
            print(count)
            return
        else:
            if "{" in args:
                self.dict_update(class_name, args)
                return
            self.onecmd(f"{command} {class_name} {args}")
            return
        super().default(arg)

    def do_create(self, arg: str) -> None:
        """creates a new instance of a class passed as argument.
        USAGE: create <class_name>"""
        args = parse_args(arg)
        if validate_args(args, 1) == -1:
            return
        if args[0] in HMIS._classes:
            new_obj = HMIS._classes[args[0]]()
            storage.new(new_obj)
            storage.save()
            print(new_obj.id)

    def do_show(self, arg: str) -> None:
        """prints the str representation of an instance.
        USAGE: <classname>.show(<id>)"""
        args = parse_args(arg)
        if validate_args(args, 2) == -1:
            return
        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            obj = storage.all()[key]
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, arg: str) -> None:
        """deletes a given instance from storage.
        USAGE: <classname>.destroy(<id>)"""
        args = parse_args(arg)
        if validate_args(args, 2) == -1:
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg: str, count=False):
        """prints all instances. USAGE: <classname>.all() or all"""
        args = parse_args(arg)
        obj_list = []
        if len(args) > 0:
            if validate_args(args, 1) == -1:
                return
            cls = HMIS._classes[args[0]]
            for obj in storage.all(cls).values():
                obj_list.append(str(obj))
            if count:
                return len(obj_list)
            print(obj_list)
            return
        for obj in storage.all().values():
            obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg: str) -> None:
        """update the given attribute of a given object.
        USAGE: <class name>.update(<id>, <attr name>, '<attr value>')
        or <classname>.update(<id>, {attr_dict})"""
        args = parse_args(arg)
        if validate_args(args, 4) == -1:
            return
        class_name, id = args[0], args[1]
        key = f"{class_name}.{id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr, value = args[2], args[3]
        obj = storage.all()[key]
        if attr in dir(obj):
            attr_type = type(getattr(obj, attr))
            obj.__dict__[attr] = attr_type(value)
        else:
            obj.__dict__[attr] = value
        obj.save()

    def dict_update(self, class_name: str, arg: str) -> None:
        pattern = re.compile(r'([\w\-]+),\s*(\{.*\})')
        res = pattern.findall(arg)
        if len(res) < 1:
            self.onecmd(f"update {class_name} {arg}")
            return
        id = res[0][0]
        obj_dict = res[0][1]
        obj_dict = obj_dict.strip("{}").split(",")
        for attr_str in obj_dict:
            attr = attr_str.split(":")
            name = attr[0].strip(' "')
            value = ""
            if len(attr) > 1:
                value = attr[1].strip(' "')
            self.onecmd(f"update {class_name} {id} {name} {value}")


def parse_args(arg: str, delim=" ") -> list:
    if arg == "":
        return []
    args = arg.split(delim)
    i = 0
    while i < len(args):
        curr = args[i].strip(",")
        found = 0
        if curr[0] == '"' and curr[-1] != '"':
            if i == len(args) - 1:
                args[i] = curr.replace('"', '')
                break
            for j in range(i + 1, len(args)):
                next = args[j]
                if next[-1] == '"':
                    found = 1
                    break
            full = curr
            for k in range(i + 1, j + 1):
                full += f" {args[k]}"
            full = full.strip('"')
            full = full.strip("'")
            args.insert(i, full)
            args_copy = args.copy()
            for k in range(i + 1, j + 2):
                args.pop(args.index(args_copy[k]))
        else:
            curr = curr.strip('"')
            args[i] = curr.strip("'")
        i += 1
    return args


def validate_args(args: list, n_args: int) -> int:
    if len(args) == 0:
        print("** class name missing **")
        return -1
    if args[0] not in HMIS._classes:
        print("** class doesn't exist **")
        return -1
    if len(args) < 2 and n_args >= 2:
        print("** instance id missing **")
        return -1
    return 0


if __name__ == "__main__":
    HMIS().cmdloop()
