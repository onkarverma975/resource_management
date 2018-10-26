addr <- maml.mapInputPort(1)
set.seed(111111)
c_size <- 100
r_size <- 10
addr <- data.frame(ADDRESS=addr[sample(1:nrow(addr), c_size+r_size),], TYPE="RELIEF-CENTER", stringsAsFactors=F)
addr$TYPE[(c_size+1):(c_size+r_size)] <- "RESOURCE-BASE"

maml.mapOutputPort("addr");