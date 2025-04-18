import { useEffect, useState } from "react";
import { motion } from "framer-motion";

const shakeVariants = {
  hidden: { x: 0 },
  visible: {
    x: [0, -5, 5, -5, 5, -3, 3, 0],
    transition: {
      duration: 0.7,
      ease: "easeInOut"
    }
  }
};

const SubmitInput = () => {
  const [startShake, setStartShake] = useState(false);

  useEffect(() => {
    setStartShake(true);
  }, []);

  return (
    <motion.button
      type="submit"
      variants={shakeVariants}
      initial="hidden"
      animate={startShake ? "visible" : "hidden"}
      className="bg-black text-white text-base rounded-2xl w-30 h-11 hover:bg-gray-900"
    >
      Notify Me
    </motion.button>
  );
};

export default SubmitInput;
