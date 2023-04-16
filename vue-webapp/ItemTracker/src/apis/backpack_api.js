var backpack_api = {
    async get_all_items(character_id) { 
        var items = []
        await fetch(`/api/items/get_all/${character_id}`, {
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
                items.push(
                    {
                        id: element["id"],
                        name: element["name"],
                        descr: element["descr"],
                        amount: element["amount"]
                    }
                )
            });
        })
        .catch(error => console.log(error))
        return items;
    },
    
    async create(name, amount, descr, character_id) {
        var result = {
            status: false,
            new_id: -1
        }
        await fetch(`/api/items/add`, {
            method: 'POST',
            body: JSON.stringify(
                {
                    name: name,
                    descr: descr ? descr : "",
                    amount: amount,
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
    },

    async set(item_id, name, amount, descr) {
        return await fetch(`/api/items/${item_id}/set`, {
            method: 'POST',
            body: JSON.stringify(
                {
                    name: name,
                    descr: descr ? descr : "",
                    amount: amount,
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
    }
  }
  
  export default backpack_api