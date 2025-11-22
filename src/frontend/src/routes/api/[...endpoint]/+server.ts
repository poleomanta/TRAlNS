import type { RequestEvent } from "./$types";

const proxy = (async ({ params, request, url, getClientAddress }: RequestEvent) => {
  const originalHeaders: HeadersInit = [...request.headers];
  let init: RequestInit = { method: request.method, body: request.body };
  // @ts-ignore
  init.duplex = "half";
  init.headers = [
    ...originalHeaders,
    //[ "X-Forwarded-For", getClientAddress() ],
  ];
  const response = await fetch(`http://127.0.0.1:8080/api/${params.endpoint + url.search}`, init).catch((error) => {
    throw error;
  });

  return response;
})

export const DELETE = proxy
export const GET = proxy;
export const PATCH = proxy;
export const POST = proxy;
export const PUT = proxy;
export const HEAD = proxy;