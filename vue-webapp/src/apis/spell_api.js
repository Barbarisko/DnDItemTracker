var spell_api = {

    async get_all_spell_levels(character_id) {
        var spell_levels = []
        await fetch(`/api/spell_levels/get_all/${character_id}`, {
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
                    spell_levels.push(
                        {
                            id: element["id"],
                            level: element["level"],
                            charges: Array.apply(0, Array(element["charges"])).map(function (x, i) { return i < element["used_charges"]; })
                        }
                    )
                    spell_levels.sort((first, second) => first.level - second.level)
                });
            })
            .catch(error => console.log(error))
        return spell_levels;
    },

    async set(level_id, level, charges, used_charges) {
        return await fetch(`/api/spell_levels/${level_id}/set`, {
            method: 'POST',
            body: JSON.stringify(
                {
                    level: level,
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

    async delete(level_id) {
        return await fetch(`/api/spell_levels/${level_id}/delete`, {
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

    async create(level, charges, used_charges, character_id) {
        var result = {
            status: false,
            new_id: -1
        }
        await fetch(`/api/spell_levels/add`, {
            method: 'POST',
            body: JSON.stringify(
                {
                    level: level,
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

export default spell_api