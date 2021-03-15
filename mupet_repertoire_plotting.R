

rm(list = ls())
setwd('C:\\Users\\Ben\\OneDrive - Duke University\\bilbo_lab\\il34_project\\il34_behavior\\usvs\\mupet_analysis\\mupet_analysis_il34_cohort_1_rerun\\20_reps_analysis\\repertoires\\CSV')


library(tidyverse)
library(ggpubr)
library(reshape2)
library(ggbeeswarm)
library(car)
library(outliers)
library(plotly)
library(ungeviz)
library(outliers)
library(rstatix)
library(readxl)
library(officer)
library(rvg)

### defining necessary functions for calculating ddCT and SEM ###
ddct <- function(x, ref) 2^(x - ref)
sem <- function(x) sqrt(var(x)/length(x))
is_outlier <- function(x) { return(x < quantile(x, 0.25) - 1.5 * IQR(x) | x > quantile(x, 0.75) + 1.5 * IQR(x)) }

z <- theme(rect = element_rect(fill = 'transparent'), 
           text = element_text(size = 50, family = 'sans'), 
           axis.line = element_line(size = 2.5),
           axis.ticks = element_line(size = 1.7),
           axis.ticks.length = unit(.5, 'cm'),
           panel.background = element_rect(fill = "transparent"), # bg of the panel
           plot.background = element_rect(fill = "transparent", color = NA), # bg of the plot
           panel.grid.major = element_blank(), # get rid of major grid
           panel.grid.minor = element_blank(), # get rid of minor grid
           legend.background = element_rect(color = NA, col = 0),  # get rid of legend bg and outline
           legend.title = element_blank(),
           axis.title.y = element_text(margin = margin(t = 0, r = 15, b = 0, l = 0), size = 30),
           axis.title.x = element_text(margin = margin(t = 15, r = 0, b = 0, l = 0)),
           strip.background = element_rect(color="transparent", fill="transparent", size=5, linetype="solid"),
           panel.spacing = unit(.5, 'cm'),
           axis.text.x = element_text(angle = 45, hjust = 1, size = 30),
           axis.text.y = element_text(hjust = 1, size = 30),
           plot.title = element_text(hjust = 0.5))



df <- read_csv("batch_rep_output.csv")



df_grouped <- df %>%
  group_by(tx, `repertoire unit (RU) number`) %>%
  summarise(dataset = mean(dataset))


ggplot(df_grouped)+
  geom_bar(stat = 'identity', aes(x = interaction(tx, `repertoire unit (RU) number`), y = dataset, fill = tx))+
  #facet_wrap(~tx)+
  z
