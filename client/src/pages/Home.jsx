import PhoneField from "../components/PhoneField";
import SubmitInput from "../components/SubmitInput";

const Home = () => {
  return (
    <div className="flex items-center justify-center relative top-60">
      <div className="flex flex-col items-center text-center">
        <div className="font-bold text-5xl">
          <h1>Get Notified for</h1>
          <h2>New Job Listings</h2>
        </div>
        <div className="text-gray-900 text-2xl mt-5">
          <p>Enter your phone number and</p>
          <p>we'll text you when new roles go</p>
          <p>live.</p>
        </div>
        <div>
            <PhoneField />
            <div className="-ml-[125px] inline-block">
                <SubmitInput />
            </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
