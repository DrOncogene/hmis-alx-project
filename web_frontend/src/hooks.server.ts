import jwt from 'jsonwebtoken'

/** @type {import('@sveltejs/kit').Handle} */
export async function handle({ event, resolve }) {
  const jwt_secret = import.meta.env.VITE_JWT_KEY
  const cookies: string = event.request.headers.get('Cookie')
  let response
  if (!cookies) {
    event.locals.user = null
    event.locals.error = 'not logged in'
    response =  await resolve(event)
    return response
  }
  let authCookie = '';
  for (const cookie of cookies.split(';')) {
    if (cookie.trim().startsWith('AuthorizationToken=Bearer')){
      authCookie = decodeURIComponent(cookie).trim()
      break
    }
  }
  authCookie = authCookie.split(' ')[1]
  
  let user;
  try {
    user = jwt.verify(authCookie, jwt_secret)
    event.locals.user = user
    event.locals.error = null
  } catch {
    event.locals.user = null
    event.locals.error = 'not logged in'
  }
  response = await resolve(event)
  return response
}