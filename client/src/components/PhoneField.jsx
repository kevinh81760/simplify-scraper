
const PhoneField = () => {
    return (
        <input
            type="tel"
            placeholder="Your phone number"
            maxLength={10}
            className="bg-white text-black text-base rounded-2xl px-3 py-3 w-105 h-14 mt-4"
        />
    )
}

export default PhoneField