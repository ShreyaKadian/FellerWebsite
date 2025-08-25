import { Link } from "@heroui/link";
import { Snippet } from "@heroui/snippet";
import { Code } from "@heroui/code";
import { button as buttonStyles } from "@heroui/theme";

import { siteConfig } from "@/config/site";
import { title, subtitle } from "@/components/primitives";
import { GithubIcon } from "@/components/icons";
import DefaultLayout from "@/layouts/default";

export default function DocsPage() {
  return (
    <DefaultLayout>
      <section className="flex flex-col items-center justify-center gap-6 py-12 md:py-16 bg-black">
        <div className="max-w-2xl text-center">
          <h1 className={title({ color: "violet" })}>Download Here</h1>
          <div className={subtitle({ class: "mt-4" })}></div>
          Download the zip and run it with ./codeine when CDed in the folder. To
          access features like mailing just add mail id and developer mail pwd
          in the env file. Mic feature is currently down in public version so
          just type!
        </div>

        <div className="flex flex-wrap gap-4 justify-center mt-6">
          <Link
            href="https://drive.google.com/drive/folders/1-W1FnYPlkCukacQl2NKIuujNBJhZcI52?usp=sharing"
            isExternal
            className={`${buttonStyles({
              radius: "full",
              variant: "shadow",
            })} 
    bg-fuchsia-600 text-white`}
          >
            Download
          </Link>
        </div>

        <div className="mt-10">
          <Snippet hideCopyButton hideSymbol variant="bordered">
            <span>
              Unzip=&gt;Go to terminal=&gt;cd into folder=&gt;just run{" "}
              <Code className="bg-fuchsia-600  text-black">./codeine</Code>
            </span>
          </Snippet>
        </div>
      </section>
    </DefaultLayout>
  );
}
