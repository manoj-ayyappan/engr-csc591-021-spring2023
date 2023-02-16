def bins(cols,rowss):
  local out = {}
  for _,col in pairs(cols) do
    local ranges = {}
    for y,rows in pairs(rowss) do
      for _,row in pairs(rows) do
        local x,k = row[col.at]
        if x ~= "?" then
          k = bin(col,x)
          ranges[k] = ranges[k] or RANGE(col.at,col.txt,x)
          extend(ranges[k], x, y) end end end
    ranges = sort(map(ranges,itself),lt"lo")
    out[1+#out] = col.isSym and ranges or mergeAny(ranges) end
  return out end