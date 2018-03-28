include ../Makefile_vars

IG_GRAPH_CONSTRUCTOR = ../ig_graph_constructor

all:
	$(MAKE) -C $(IG_GRAPH_CONSTRUCTOR)
	$(MAKE) $(DENSE_SUBGRAPHS)

$(DENSE_SUBGRAPHS): $(IG_GRAPH_CONSTRUCTOR)/$(SW_GRAPH) $(IGREC)/dense_subgraph_finder.py
	$(IGREC)/dense_subgraph_finder.py \
	--graph $(IG_GRAPH_CONSTRUCTOR)/$(SW_GRAPH) \
	--output . \
	--threads 16 \
	--min-snode-size 1000000 \
	--min-fillin 0.6 \
	--no-clean-output-dir

clean:
	$(RM) $(DENSE_SUBGRAPHS)
	$(MAKE) -C $(IG_GRAPH_CONSTRUCTOR) clean
