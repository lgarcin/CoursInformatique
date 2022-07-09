import subprocess
import os

from livereload import Server


def main():
    def build():
        subprocess.run(["jb", "clean", "."])
        subprocess.run(["jb", "build", "."])

    if not os.path.exists("_build/html"):
        build()

    server = Server()

    server.watch("source/**/*.md", build)
    server.watch("source/**/*.ipynb", build)
    server.watch("source/**/*.rst", build)
    server.watch("_config.yml", build)
    server.watch("_toc.yml", build)

    server.serve(root="_build/html", port=8002)


if __name__ == "__main__":
    main()
