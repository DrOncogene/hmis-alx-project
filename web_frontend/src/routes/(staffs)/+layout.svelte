<script lang="ts">
  import { page } from '$app/stores';
  import ForwardBurger from 'svelte-material-icons/Forwardburger.svelte'
  import BackBurger from 'svelte-material-icons/Backburger.svelte'
  import profileImg from '$lib/assets/doc.jpg'
  import Menu from '$lib/components/Menu.svelte';
  import Button from '$lib/components/Button.svelte';
  import { toggleMenu } from '$lib/utils'

  /** @type import('./$types').LayoutData */
  export let data

  $: staffName = `${data.user.title} ${data.user.first_name} ${data.user.last_name}`
</script>

<aside class="side-menu hidden md:flex flex-col justify-start items-center w-[400px] h-[100vh] bg-pri fixed top-0 left-0 transition-all duration-[600ms]">
  <div class="text-center mt-10 flex flex-col space-y-5 justify-center items-center">
    <img src="{profileImg}" loading="lazy" alt="" class="block w-40 h-40 rounded-full">
    <h4 class="font-bold text-xl">{staffName}</h4>
    <h6 class="text-sm italic">Family Medicine</h6>
  </div>
  <Menu menuItems={$page.data.items} />
</aside>
<section class="right flex flex-col space-y-5 md:ml-[400px] transition-all duration-[500ms] h-[100vh]">
  <nav class="sticky top-0 z-[500] w-full bg-[#ddd2d0] border-b-2 border-b-pri h-[50px] px-4 flex justify-between items-center">
    <span on:click={e => {toggleMenu(e)}} on:keypress={e => {toggleMenu(e)}} class="menu-toggle flex justify-center items-center cursor-pointer">
      <i class="menu-close"><BackBurger color="#886C63" size="2.5em" /></i>
      <i class="menu-open hidden"><ForwardBurger color="#886C63" size="2.5em" /></i>
    </span>
    <div class="flex space-x-6 items-center">
      <p class="text-pri font-bold text-sm">{staffName}</p>
      <img src="{profileImg}" alt="" class="w-[30px] h-[30px] rounded-full">
      <form action="/?/logout" method="POST">
        <Button
          text="LOGOUT"
          dim={['px-4', 'py-2']}
          type='submit'
        />
      </form>
    </div>
  </nav>
  <slot></slot>
</section>

<style>

</style>