var utils = {

    calculate_used_charges(charges) {
        return charges.reduce((total, x) => total + (x), 0)
    },

    async sha256(message) {
        if (crypto.subtle) {

            // encode as UTF-8
            const msgBuffer = new TextEncoder().encode(message);

            // hash the message
            const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);

            // convert ArrayBuffer to Array
            const hashArray = Array.from(new Uint8Array(hashBuffer));

            // convert bytes to hex string                  
            const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
            return hashHex;
        }

        // will use this until https configured 
        let hash = 0;
        for (let i = 0; i < message.length; i++) {
            hash = (hash << 5) - hash + message.charCodeAt(i);
            hash |= 0; // Convert to 32bit integer
        }
        return String(hash);
    },
    intToRoman(num) {
        if (isNaN(num))
            return NaN;
        if (num == 1)
            return "I";
        if (num == 2)
            return "II";
        if (num == 3)
            return "III";
        var digits = String(+num).split(""),
            key = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM",
                "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC",
                "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
            roman = "",
            i = 3;
        while (i--)
            roman = (key[+digits.pop() + (i * 10)] || "") + roman;
        var res = Array(+digits.join("") + 1).join("M") + roman;
        return res;
    }
}

export default utils