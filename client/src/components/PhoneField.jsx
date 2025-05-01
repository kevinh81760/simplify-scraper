const PhoneField = ({ value, onChange }) => {
    return (
      <input
        type="tel"
        value={value}
        onChange={onChange} // updates parent state when user types
        placeholder="Your phone number"
        maxLength={10}
        className="bg-white text-black text-base rounded-2xl px-3 py-3 w-105 h-14 mt-4 focus:outline-none focus:ring-0"
      />
    );
  };
  
  export default PhoneField;
  