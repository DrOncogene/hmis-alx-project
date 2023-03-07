import { redirect, invalid } from "@sveltejs/kit";
import type { RequestEvent, Actions } from "./$types";
import jwt from 'jsonwebtoken'
import { validateEmail } from "$lib/utils";

export function load (event: RequestEvent) {
  const user = event.locals.user
  if (user) {
    throw redirect(303, `/${user.staff_type}s`)
  } 
  if (event.locals.error === 'not logged in') {
    return {error: true}
  } else {
    return {error: false}
  }
}

/** @type {import('./$types').Actions} */
export const actions: Actions = {
  login: async ( event: RequestEvent) => {
    // TODO log the user in
    const loginData = await event.request.formData().then(res => res)
    const value = loginData.get('user')
    const passwd = loginData.get('password')
    let credentials = {}
    if (validateEmail(value)) {
      credentials = {email: value, password: passwd}
    } else {
      credentials = {username: value, password: passwd}
    }
    const resp = await fetch("http://127.0.0.1:5000/auth/login", {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': "localhost:5000",
        'Access-Control-Allow-Credentials': "true",
      },
      credentials: 'include',
      body: JSON.stringify(credentials)
    })
    .then(res => res)

    if (resp.status !== 200) {
      return invalid(400, {value, passwd, invalid: true})
    }
    
    const cookieHeader = resp.headers.get('set-cookie')
    const respCookies = cookieHeader?.split(';')
    respCookies?.forEach((cookie) => {
      const name = cookie.split('=')[0]
      const val = cookie.split('=')[1]
      event.cookies.set(name, val)
    })
    const payload = await resp.json()
    const user = payload.user

    const jwt_secret: string = import.meta.env.VITE_JWT_KEY
    const token = jwt.sign(user, jwt_secret, {expiresIn: "12h"})
    event.cookies.set('AuthorizationToken', `Bearer ${token}`, {
      httpOnly: true,
      path: '/',
      sameSite: 'strict',
      maxAge: 60 * 60 * 12
    })
    throw redirect(303, `/${user.staff_type}s`)
  },
  logout: async (event: RequestEvent) => {

    const url = 'http://127.0.0.1:5000/auth/logout'
    const cookies = event.request.headers.get('Cookie')
    const response = await fetch(url, {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Access-Control-Allow-Origin': "localhost:5000",
        'Access-Control-Allow-Credentials': "true",
        'Cookie': decodeURIComponent(cookies)
      },
      credentials: 'include',
    })
    .then(res => res)
    const loggedOut = await response.json()
    if (loggedOut.logout === true) {
      // return an empty token to override the existing one, simulating a log out
      event.cookies.set('AuthorizationToken', `Bearer `, {
        httpOnly: true,
        path: '/',
        sameSite: 'strict',
        maxAge: 5
      })
      throw redirect(301, "/")
    }
  }
};

const decodeJwt = (reqCookie: string) => {
  const jwt_secret = import.meta.env.VITE_JWT_KEY
  const cookies: string[] = reqCookie.split(';')
  let authCookie = '';
  for (const cookie of cookies) {
    if (cookie.trim().startsWith('AuthorizationToken=Bearer')){
      authCookie = decodeURIComponent(cookie).trim()
      break
    }
  }
  authCookie = authCookie.split(' ')[1]
  let user;
  try {
    user = jwt.verify(authCookie, jwt_secret)
    return user
  } catch {
    return 'error: invalid token'
  }
}
