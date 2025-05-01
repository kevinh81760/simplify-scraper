import { useState } from "react"
import axios from "axios"
import PhoneField from "./PhoneField"
import SubmitInput from "./SubmitInput"

const PhoneForm = () => {
  const [phone, setPhone] = useState("")
  const [startShake, setStartShake] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()

    setStartShake(true)     // ✅ Trigger the animation
    setTimeout(() => setStartShake(false), 700)  // ✅ Reset for next time

    try {
      await axios.post("http://localhost:5000/api/phone", {
        number: phone,
      })
      alert("Phone number submitted!")
      setPhone("")
    } catch (err) {
      console.error(err)
      alert("Error submitting number")
    }
  }

  return (
    <form onSubmit={handleSubmit} className="flex flex-col gap-4">
      <PhoneField value={phone} onChange={(e) => setPhone(e.target.value)} />
      <SubmitInput startShake={startShake} />
    </form>
  )
}

export default PhoneForm
