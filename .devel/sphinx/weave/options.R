# Copyright (C) 2020-2022, Marek Gagolewski <https://www.gagolewski.com>

options(encoding="UTF-8")
set.seed(666)
options(width=74)
options(digits=5)
options(stringsAsFactors=FALSE)  # default in R 4.0
options(max.print=99)
options(useFancyQuotes=FALSE)
reticulate::use_python("/usr/bin/python3")
options(warnPartialMatchArgs=TRUE)
options(warnPartialMatchAttr=TRUE)
options(warnPartialMatchDollar=TRUE)

################################################################################

library("knitr")
library("stringi")

# knit_engines$set(python = reticulate::eng_python)

#opts_chunk$set(engine = 'python')

opts_chunk$set(
    dev="pdf",
    fig.width=5.9375,    # /1.25 = (textwidth=4.75)
    out.width=5.9375,
    fig.height=3.4635,  # fig.width/(12/7)
    dpi=240,            # *1.5 = 300
    dev.args=list(pointsize=13),
    #dev=c("CairoPDF", "CairoSVG"),
    error=FALSE,
    fig.show="hold",
    results="hold",
    fig.lp='fig:',
    autodep=FALSE,
    cache=FALSE,
    comment="##",
    cache.comments=TRUE
    #python.reticulate=FALSE
)

# opts_chunk$set(
#    #engine.opts=list(python="-c"),
#     engine.path=list(python="/usr/bin/python3")
# )

hook_plot_md_pandoc_new <- function (x, options)
{
    if (options$fig.show == "animate")
        return(hook_plot_html(x, options))
    file <- stri_replace_first_regex(x, "\\.(pdf|png|jpg|svg|svgz)", ".*")
    base <- opts_knit$get("base.url") %n% ""
    cap <- .img.cap(options)
# #     cap <- sprintf("(\\#fig:%s) %s", options[["label"]], cap)
#     at <- paste(c(
#         #sprintf("#fig:%s", options[["label"]]),  # Marek's hack
#         sprintf("width=%s", options[["out.width"]]),
#         sprintf("height=%s", options[["out.height"]]), options[["out.extra"]]),
#         collapse = " ")
#     if (at != "") {
#         at = paste0("{", at, "}")
#     }
#     sprintf("![%s](%s)%s", cap, file, at)


    sprintf("(fig:%s)=\n```{figure} %s\n%s\n```", options[["label"]], file, cap)
}

environment(hook_plot_md_pandoc_new) <- environment(knitr:::hook_plot_md_pandoc)
unlockBinding("hook_plot_md_pandoc", getNamespace("knitr"))
assign("hook_plot_md_pandoc", hook_plot_md_pandoc_new, getNamespace("knitr"))

knit_hooks$set(plot=knitr:::hook_plot_md_pandoc)

################################################################################
