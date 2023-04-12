var consumable_api = {

    async get_all_consumables(character_id) {
        var consumables = []
        await fetch(`/api/consumables/get_all/${character_id}`, {
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
                    consumables.push(
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
        return consumables;
    },

    async create(name, amount, descr, character_id) {
        var result = {
            status: false,
            new_id: -1
        }
        await fetch(`/api/consumables/add`, {
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

    async set(consumable_id, name, amount, descr) {
        return await fetch(`/api/consumables/${consumable_id}/set`, {
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

export default consumable_api