import sdk from '@api/memgpt';

sdk.list_humans_api_humans_get()
  .then(({ data }) => console.log(data))
  .catch(err => console.error(err));