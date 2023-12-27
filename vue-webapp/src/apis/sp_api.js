var sp_api = {

    async get_all_special_powers(character_id) { 
        var special_power = []
        await fetch(`/api/special_powers/get_all/${character_id}`, {
            method: 'GET',
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
            data.forEach(element => {
                special_power.push(
                    {
                        id: element["id"],
                        name: element["name"],
                        charges: Array.apply(0, Array(element["charges"])).map(function (x, i) { return i < element["used_charges"]; })
                    }
                )
                special_power.sort((first, second) => first.id - second.id)
            });
        })
        .catch(error => console.log(error))
        return special_power;
    },

    async set(power_id, name, charges, used_charges) {
        return await fetch(`/api/special_powers/${power_id}/set`, {
            method: 'POST',
            body: JSON.stringify(
                {
                    name: name,
                    charges: charges,
                    used_charges: used_charges
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
            return true
        })
        .catch(error => {
            console.log(error)
            return false
        })
    },

    async delete(power_id) {
        return await fetch(`/api/special_powers/${power_id}/delete`, {
            method: 'DELETE',
            body: JSON.stringify(
                {
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
                return true
            })
            .catch(error => {
                console.log(error)
                return false
            })
    },

    async create(name, charges, used_charges, character_id) {
        var result = {
            status: false,
            new_id: -1
        }
        await fetch(`/api/special_powers/add`, {
            method: 'POST',
            body: JSON.stringify(
                {
                    name: name,
                    charges: charges,
                    used_charges: used_charges,
                    character_id: character_id
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
    }
  }
  
  export default sp_api