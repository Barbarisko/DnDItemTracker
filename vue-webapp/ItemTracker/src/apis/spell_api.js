var spell_api = {

    async get_all_spell_levels(character_id) { 
        var spell_levels = []
        await fetch(`http://127.0.0.1:5000/api/spell_levels/get_all/${character_id}`, {
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
                spell_levels.push(
                    {
                        id: element["id"],
                        level: element["level"],
                        charges: Array.apply(0, Array(element["charges"])).map(function (x, i) { return i < element["used_charges"]; })
                    }
                )
            });
        })
        .catch(error => console.log(error))
        return spell_levels;
    }

  }
  
  export default spell_api