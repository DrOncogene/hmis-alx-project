import { redirect} from "@sveltejs/kit";

/** @type {import('./$types').LayoutServerLoad} */
export async function load({ parent }) {
  const {user, csrf} = await parent()
  if (!user) {
    throw redirect(301, '/')
  }

  return {
    user: user,
    csrf: csrf
  }
}