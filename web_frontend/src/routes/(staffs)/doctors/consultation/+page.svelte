<script lang="ts">
  import FormInput from "$lib/components/FormInput.svelte";
  import Tabs from "$lib/components/Tabs.svelte";

  export let data;
</script>

<div class="w-full text-pri flex flex-col space-y-10 items-center">
  <FormInput
    ph='Hospital Number'
    dim={['px-5', 'py-2']}
    type='text'
    name='pid'
    cls='w-[400px] text-pri'
  />
  <div class="relative grid grid-cols-3 border-2 border-pri w-3/4 p-8 gap-2">
      <p class="absolute -top-5 left-3 bg-white p-2">Patient Details</p>
      <div>
        <p>Name:</p>
        <p>Name:</p>
      </div>
      <div>
        <p>Name:</p>
        <p>Name:</p>
      </div>
      <div>
        <p>Name:</p>
        <p>Name:</p>
      </div>
  </div>
  <div class="relative w-3/4 h-[500px] border border-pri overflow-y-scroll scroll-m-0">
    <Tabs
      items= {[
        {
          text: 'Consultation',
          curr: true
        },
        {
          text: 'Prescription',
          curr: false
        },
        {
          text: 'E-Folder',
          curr: false
        },
      ]}
    />

  </div>
</div>