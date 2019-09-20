#!/bin/bash

docker run --rm -tid -v $(pwd)/samples:/samples --name epub2pdf1 epub2pdf
