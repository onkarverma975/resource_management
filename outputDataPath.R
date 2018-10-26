library(TSP)
library(stringi)
library(dplyr)

location <- maml.mapInputPort(1)

# Compute optimal path (shortest manhattan distance) for each relief center address cluster
paths <- list()
distances <- list()
n_cluster <- length(location$TYPE[location$TYPE == "RESOURCE-BASE"])
for(i in 1:n_cluster) {
  x <- dist(location[location$GROUP==i, colnames(location) %in% c("X","Y","Z")], method="manhattan", diag=T, upper=T)
  x1 <- as.matrix(x)
  rownames(x1) <- location[location$GROUP==i, "ID"]
  colnames(x1) <- location[location$GROUP==i, "ID"]
  tsp <- as.TSP(x1)
  atsp <- as.ATSP(tsp)
  v <- which(stri_startswith_fixed(labels(tsp), "R"))
  atsp[, v] <- 0
  path <- solve_TSP(atsp, method="farthest_insertion")
  path <- cut_tour(path, v, exclude_cut=F)
  paths[[i]] <- path
  distances[[i]] <- x1
}

# Organize the data for each computed path to present the information in terms of start location, end location, sequence number, and distance
data_path <- data.frame()
for(i in 1:length(paths)) {
  for(j in 1:(length(paths[[i]])-1)) {
    d <- distances[[i]]
    from <- labels(paths[[i]][j])
    to <- labels(paths[[i]][j+1])
    type <- "RELIEF-CENTER"
    if(stri_startswith_fixed(from, "R")) {
      type <- "RESOURCE-BASE"
    }
    lat_from <- location$LATITUDE[location$ID == from]
    lon_from <- location$LONGITUDE[location$ID == from]
    lat_to <- location$LATITUDE[location$ID == to]
    lon_to <- location$LONGITUDE[location$ID == to]
    data_path <- rbind(data_path, data.frame(GROUP=i, FROM=from, TO=to, SEQUENCE=j, DISTANCE=d[from, to], TYPE=type,
                                             LAT_FROM=lat_from, LON_FROM=lon_from, LAT_TO=lat_to, LON_TO=lon_to))
  }
}

maml.mapOutputPort("data_path")