const esc = encodeURIComponent;

const defaultHeaders = {
  'content-type': 'application/json',
};

export function addDefaultHeader(key, value) {
  defaultHeaders[key] = value;
}

export function removeDefaultHeader(key) {
  delete defaultHeaders[key];
}

function buildQueryString(params) {
  const parts = Object.keys(params).map(k => `${esc(k)}=${esc(params[k])}`);
  return `?${parts.join('&')}`;
}

export function request(url, method, body = null, queryParams = {}, headers = {}) {
  const requestConfig = {
    method,
    headers: {
      ...defaultHeaders,
      ...headers,
    },
  };

  if (body !== null && requestConfig.headers['content-type'] === 'application/json') {
    requestConfig.body = JSON.stringify(body);
  } else {
    requestConfig.body = body;
  }

  if (Object.keys(queryParams).length > 0) {
    url = `${url}?${buildQueryString(queryParams)}`;
  }

  return fetch(url, requestConfig);
}

export function get(url, queryParams, headers = {}) {
  return request(url, 'GET', null, queryParams, headers);
}

export function post(url, body = {}, headers = {}) {
  return request(url, 'POST', body, {}, headers);
}

export function put(url, body = {}, headers = {}) {
  return request(url, 'PUT', body, {}, headers);
}

export function del(url, body = {}, headers = {}) {
  return request(url, 'DELETE', body, {}, headers);
}
