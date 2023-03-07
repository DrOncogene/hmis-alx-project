import type { RequestEvent } from "./$types"

export function load (event: RequestEvent) {
  const user = event.locals.user
  return {
    user: user,
    items: [
      {
        text: "Consultation",
        link: `/${user.staff_type}s/consultation`
      },
      {
        text: "E-Folder",
        link: `/${user.staff_type}s/e-folder`
      },
      {
        text: "Prescription",
        link: `/${user.staff_type}s/prescription`
      },
      {
        text: "Edit",
        link: `/${user.staff_type}s/edit`
      },
      {
        text: "Referral",
        link: `/${user.staff_type}s/referral`
      },
    ]
  }
}