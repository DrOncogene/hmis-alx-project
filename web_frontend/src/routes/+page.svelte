<script lang="ts">
  import { fly } from 'svelte/transition'
	import { enhance } from '$app/forms';
  import LockOutline from 'svelte-material-icons/LockOutline.svelte'
  import AccountOutline from 'svelte-material-icons/AccountOutline.svelte'
  import EyeOutline from 'svelte-material-icons/EyeOutline.svelte'
  import EyeOffOutline from 'svelte-material-icons/EyeOffOutline.svelte'
  import MapMarkerRadius from 'svelte-material-icons/MapMarkerRadius.svelte'
  import caduceus from '$lib/assets/caduceus.svg';
  import hmisLogo from '$lib/assets/hmis-logo.svg';
  import FormInput from '$lib/components/FormInput.svelte';
  import Button from '$lib/components/Button.svelte';
  import { togglePasswdInput } from '$lib/utils'

  /** @type { import('./$types').ActionData } */
  export let form;
  export let data;

  const hospital: string = import.meta.env.VITE_HOSP_NAME
  const address: string = import.meta.env.VITE_HOSP_ADDRR

  const closeError = () => {
    form.invalid = false
  }
</script>

<div class="lg:grid lg:grid-cols-default">
  <section class="hidden lg:flex flex-col justify-start items-center p-6 h-[100vh] bg-pri">
    <div class="flex justify-center items-center bg-white h-[200px] w-[200px] rounded-full shadow-xl mb-10">
      <img src="{caduceus}" alt="The Caduceus" class="w-[100px] h-[100px]" />
    </div>
    <p class="text-white font-bold text-3xl text-center">WELCOME TO {hospital.toUpperCase()}</p>
    <footer class="text-white font-light text-sm flex items-center justify-center space-x-3 mt-auto">
      <MapMarkerRadius size="1.5em" />
      <p>{address}</p>
    </footer>
  </section>
  <section class="flex flex-col justify-start p-6 items-center bg-homeBg bg-gray-800 bg-cover bg-no-repeat h-[100vh] bg-blend-overlay">
    <img src="{hmisLogo}" alt="" class="justify-self-start mb-10 opacity-10"/>
    <p class="text-2xl text-pri font-bold text-center mb-10">STAFF LOG IN</p>
    <form action="?/login" method="POST" use:enhance class="login-form flex flex-col justify-center items-center space-y-10">
      {#if form?.invalid}
        <p transition:fly={{y:-10, duration:500}} class="error-popup relative text-red-500 text-sm text-center border-red-800 w-[250px] bg-lightPri py-2 px-3 rounded-lg self-end">
          Invalid username or password
          <span on:click={closeError} on:keypress={closeError} class="error-close absolute top-0 right-2 text-red-500 text-2xl leading-none cursor-pointer">&times;</span>
        </p>
      {/if}
      <FormInput
      label={[true, "Username/Email"]}
      dim={['px-10', 'py-2']}
      ph="Username/Email"
      type="text"
      name="user"
      >
        <i slot="left-icon" class="absolute top-2 left-40 flex"><AccountOutline size="1.5em" color="#886C63" /></i>
      </FormInput>
      <FormInput
        label={[true, "Password"]}
        dim={['px-10', 'py-2']}
        ph="Password"
        type="password"
        name="password"
      >
        <i slot="left-icon" class="absolute top-2 left-40 flex"><LockOutline size="1.5em" color="#886C63" /></i>
        <span slot="right-icon" on:click={togglePasswdInput} on:keypress={togglePasswdInput} class="passwd-toggle absolute top-3 right-4 cursor-pointer">
          <i class="transition-[display] duration-[1s] w-5 h-4"><EyeOutline color="#886C63" /></i>
          <i class="hidden transition-[display] duration-500"><EyeOffOutline color="#886C63" /></i>
        </span>
      </FormInput>
      <div class="flex justify-between items-center w-2/3 ml-auto text-white">
        <a href="#" class="italic font-thin text-sm border-b border-transparent hover:border-b hover:border-b-sec">forgot password?</a>
        <Button
        text="SIGN IN"
        dim={['px-4', 'py-2']}
        cls=''
        />
      </div>
    </form>
  </section>
</div>
