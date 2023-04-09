var character_api = {

    async get_all_characters(user_id) {
        var characters = []
        await fetch(`/api/character/get_all/${user_id}`, {
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
                    characters.push(
                        {
                            id: element["id"],
                            name: element["name"],
                            level: element["level"],
                            class_name: element["class_name"]
                        }
                    )
                });
            })
            .catch(error => console.log(error))
        return characters;
    },

    async create(name, level, class_name, user_id) {
        var result = {
            status: false,
            new_id: -1
        }
        await fetch(`/api/character/add`, {
            method: 'POST',
            body: JSON.stringify(
                {
                    name: name,
                    level: level, 
                    class_name: class_name,
                    user_id: user_id
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
export default character_api