#!/bin/bash

docker run --rm -tid -v $(pwd)/samples:/samples --name epub2pdf1 -p 1337:1337 epub2pdf
