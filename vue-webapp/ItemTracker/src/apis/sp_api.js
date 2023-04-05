var sp_api = {

    async get_all_special_powers(character_id) { 
        var special_power = []
        await fetch(`http://127.0.0.1:5000/api/special_powers/get_all/${character_id}`, {
            method: 'GET',
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
        return await fetch(`http://127.0.0.1:5000/api/special_powers/${power_id}/set`, {
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
        .then(response => {
            // indicates whether the response is successful (status code 200-299) or not
            if (!response.ok) {
                throw new Error(`Request failed with status ${reponse.status}`)
            }
            return true
        })
        .catch(error => {
            console.log(error)
            return false
        })
    }

  }
  
  export default sp_api