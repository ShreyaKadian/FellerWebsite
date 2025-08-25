import { Link } from "@heroui/link";
import { Snippet } from "@heroui/snippet";
import { Code } from "@heroui/code";
import { button as buttonStyles } from "@heroui/theme";

import { siteConfig } from "@/config/site";
import { title, subtitle } from "@/components/primitives";
import { GithubIcon } from "@/components/icons";
import DefaultLayout from "@/layouts/default";

export default function IndexPage() {
  return (
    <DefaultLayout>
      <section className="flex flex-col items-center justify-center gap-4 py-8 md:py-10">
        <div className="inline-block max-w-xl text-center justify-center">
          <span className={title()}>Welcome to&nbsp;</span>
          <span className={title({ color: "violet" })}>Feller&nbsp;</span>
          <div className={subtitle({ class: "mt-4" })}>
            Feller is a software that is upposed to be your perfect digital
            assistant. The goal of the software is to make your computing
            experience completely handless. It is operated by voice and can
            perform almost all the Tasks u might use a computer for. Presently
            its for Linux only (Mic feature is currently inactive in the public
            version). Below are all the actions it can perform and all the commands for it 
          </div>
          <br></br>
          <span className={title({ color: "violet" })}>Demo&nbsp;</span>
          <br></br> <br></br>


          
          <video className="w-full rounded-xl shadow-lg" controls>
            <source src="fellasblack.mp4" type="video/mp4" />
            <track
              kind="captions"
              srcLang="en"
              label="English captions"
              src="captions.vtt"
              default
            />
            Your browser does not support the video tag.
          </video>



          <br></br> <br></br>
          <span className={title({ color: "violet" })}>
            Activities it can perform -&nbsp;
          </span>
          <div className={subtitle({ class: "mt-4" })}>
            <ul className="list-disc">
              <li>Open any software in your computer (Spotify,Photoshop)-open x</li>
              <li>Open any website-open x.com / open a website</li>
              <li>Make any Notes that it will remember-make a note</li>
              <li>
                Open any file in your computer with just a bit of the name(image
                , text , video) - open a file
              </li>
              <li>Set reminders - set a reminder</li>
              <li>Send instagram dms - send a dm</li>              
              <li>Make,save,edit,read any text file - open a file/edit a file/read a file/make a file</li>
              <li>Send an email-send email</li>
              <li>Read/summarise daily emails-check email</li>
              <li>Make and show a daily todo list-make/show a todo list</li>
              <li>Make and show a daily appointments list-make/show an appointment</li>
              <li>Access all features of ai assistants like Groq - say anything if you are using a keyword just go to chatmode and it wont pick up any command words</li>
              <li>Search anything on youtube</li>
              {/* <li>open any youtube channel just by youtubers name</li> */}
              <li>Take screenshots</li>
            </ul>
          </div>
          <br></br>
          <span className={title({ size: "sm" })}>Go to the&nbsp;</span>
          <a
            href="/download"
            className="underline decoration-[#9d2cb4] decoration-3 underline-offset-3"
          >
            <span className={title({ color: "violet", size: "sm" })}>
              download page&nbsp;
            </span>
          </a>
          <span className={title({ size: "sm" })}>
            {" "}
            to get the assistant for yourself (Linux only) &nbsp;
          </span>
        </div>

        {/* <div className="flex gap-3">
          <Link
            isExternal
            className={buttonStyles({
              color: "primary",
              radius: "full",
              variant: "shadow",
            })} */}
        {/* //href={siteConfig.links.docs}
          >
            Documentation
          </Link> */}
        {/* <Link
            isExternal
            className={buttonStyles({ variant: "bordered", radius: "full" })}
            href={siteConfig.links.github}
          >
            <GithubIcon size={20} />
            GitHub
          </Link> */}
        {/* </div> */}

        {/* <div className="mt-8">
          <Snippet hideCopyButton hideSymbol variant="bordered">
            <span>
              Get started by editing{" "}
              <Code color="primary">pages/index.tsx</Code>
            </span>
          </Snippet>
        </div> */}
      </section>
    </DefaultLayout>
  );
}
