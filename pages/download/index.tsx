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
      <section className="flex flex-col items-center justify-center gap-6 py-12 md:py-16">
        <div className="max-w-2xl text-center">
          <h1 className={title()}>Download Here</h1>

          <div className={subtitle({ class: "mt-4" })}>
            Feller is a software that aims to be your perfect digital assistant.
            It’s designed to make your computing experience completely hands-free.
            Operated by voice, it can perform nearly all tasks you use a computer for.
            Currently available for Linux only.
          </div>
        </div>

        <div className="flex flex-wrap gap-4 justify-center mt-6">
          <Link
            isExternal
           // href={siteConfig.links.home}
            className={buttonStyles({
              color: "primary",
              radius: "full",
              variant: "shadow",
            })}
          >
            Documentation
          </Link>

          <Link
            isExternal
            href={siteConfig.links.github}
            className={buttonStyles({
              variant: "bordered",
              radius: "full",
            })}
          >
            <GithubIcon size={20} />
            GitHub
          </Link>
        </div>

        <div className="mt-10">
          <Snippet hideCopyButton hideSymbol variant="bordered">
            <span>
              Get started by editing{" "}
              <Code color="primary">pages/index.tsx</Code>
            </span>
          </Snippet>
        </div>
      </section>
    </DefaultLayout>
  );
}
