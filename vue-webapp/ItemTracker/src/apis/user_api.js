var user_api = {

  async create(username, password_hash) {
    var result = {
      status: false,
      message: "",
      new_id: -1
    }
    await fetch(`/api/user/create`, {
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
      .then(responce => {
        // indicates whether the responce is successful (status code 200-299) or not
        if (!responce.ok) {
          throw new Error(`Request failed with status ${responce.status}`)
        }
        return responce.json()
      })
      .then(data => {
        result.status = true;
        result.new_id = data['id'];
      })
      .catch(error => console.log(error))
      return result
  },

  async login(username, password_hash) {
    var result = {
      status: false,
      message: "",
      new_id: -1
    }
    await fetch(`/api/user/login`, {
      method: 'POST',
      body: JSON.stringify(
        {
          username: username,
          password_hash: password_hash
        }
      ),
      headers: {
        'Content-type': 'application/json; charset=UTF-8'
      }
    })
      .then(responce => {
        debugger
        // indicates whether the responce is successful (status code 200-299) or not
        if (!responce.ok) {
          if(responce.status == 500)
          {
            result.message = "Invalid username or password. "
          }
          throw new Error(`Request failed with status ${responce.status}`)
        }
        return responce.json()
      })
      .then(data => {
        result.status = true;
        result.new_id = data['id'];
      })
      .catch(error => {
        console.log(error); 
        debugger
      })
      return result
  }

}

export default user_api