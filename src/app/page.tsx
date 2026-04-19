import Nav from "@/components/ui/Nav";
import Footer from "@/components/ui/Footer";
import Hero from "@/components/sections/Hero";
import RecruitingReality from "@/components/sections/RecruitingReality";
import MeetNikki from "@/components/sections/MeetNikki";
import HowItWorks from "@/components/sections/HowItWorks";
import BuiltByCoach from "@/components/sections/BuiltByCoach";
import Pricing from "@/components/sections/Pricing";
import FinalCTA from "@/components/sections/FinalCTA";

export default function Home() {
  return (
    <>
      <Nav />
      <main>
        <Hero />
        <RecruitingReality />
        <MeetNikki />
        <HowItWorks />
        <BuiltByCoach />
        <Pricing />
        <FinalCTA />
      </main>
      <Footer />
    </>
  );
}
