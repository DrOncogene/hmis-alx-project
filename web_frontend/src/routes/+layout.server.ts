import type { ServerLoadEvent } from "@sveltejs/kit"

/** @type {import('./$types').LayoutServerLoad} */
export async function load(event: ServerLoadEvent) {
  const csrfToken = await fetch("http://127.0.0.1:5000/auth/getcsrf", {
    credentials: 'same-origin'
  })
  .then(resp => {
    const csrfToken: string | null = resp.headers.get('X-CSRFToken')
    return {
      csrf: csrfToken
    }
  })
  .catch(() => {
    return {
      csrf: {err: 'Failed to get csrf token...'}
    }
  })
  const url = event.url

  return {
    user: event.locals.user,
    csrf: csrfToken?.csrf
  }
}