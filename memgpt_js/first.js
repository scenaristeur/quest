import sdk from '@api/memgpt';

//const sdk = require('@api/memgpt');

sdk.auth('ilovellms');
sdk.server('http://localhost:8283');
sdk.get_all_users_admin_users_get()
  .then(({ data }) => console.log(data))
  .catch(err => console.error(err));


  