var user_api = {

  async create(username, password_hash) {
    result = {
      status: false,
      new_id: -1
    }
    await fetch(`http://127.0.0.1:5000/api/user/create/`, {
      method: 'POST',
      body: JSON.stringify(
        {
          username: username,
          password_hash: password_hash,
          is_pidr: true
        }
      ),
      headers: {
        'Content-type': 'application/json; charset=UTF-8'
      }
    })
      .then(response => {
        // indicates whether the response is successful (status code 200-299) or not
        if (!response.ok) {
          throw new Error(`Request failed with status ${reponse.status}`)
        }
        return response.json()
      })
      .then(data => {
        result.status = true;
        result.new_id = data['id'];
      })
      .catch(error => console.log(error))
      return result
  },

  async login(username, password_hash) {
    result = {
      status: false,
      new_id: -1
    }
    await fetch(`http://127.0.0.1:5000/api/user/login/`, {
      method: 'POST',
      body: JSON.stringify(
        {
          username: username,
          password_hash: password_hash,
        }
      ),
      headers: {
        'Content-type': 'application/json; charset=UTF-8'
      }
    })
      .then(response => {
        // indicates whether the response is successful (status code 200-299) or not
        if (!response.ok) {
          throw new Error(`Request failed with status ${reponse.status}`)
        }
        return response.json()
      })
      .then(data => {
        result.status = true;
        result.new_id = data['id'];
      })
      .catch(error => console.log(error))
      return result
  }

}

export default user_api