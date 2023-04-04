var utils = {

    calculate_used_charges(charges) {
        return charges.reduce((total,x) => total+(x), 0)
    }
}

export default utils