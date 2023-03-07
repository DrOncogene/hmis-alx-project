<script lang="ts">
  import "../app.css"
  
  /** @type {import('./$types').LayoutData} */
  export let data
</script>

<svelte:head>
  <title>Sign in | HMIS </title>
</svelte:head>

<main class="w-100vw h-[100vh]" id="main-container">
  <input type="hidden" name="csrf-token" id="csrf-token" value="{data.csrf}">
  <slot></slot>
</main>
