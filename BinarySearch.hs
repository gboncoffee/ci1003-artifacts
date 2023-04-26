binarySearch' item list oldidx
           | cur > item = binarySearch' item fh oldidx
           | cur < item = binarySearch' item sh $ oldidx + idx
           | otherwise = oldidx + idx
           where 
                idx = ((length list) `div` 2)
                cur = list !! idx
                (fh, sh) = splitAt idx list

binarySearch item list = binarySearch' item list 0

main = print $ binarySearch 1 [1,2,3,4,5,6,7,8,9]
