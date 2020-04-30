# Convert MNIST bin to text data
#
# Copyright (C) 2015-2020 Marek.Gagolewski.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.



f <- file('t10k-labels-idx1-ubyte', 'rb')
stopifnot(readBin(f, 'integer', 1L, endian='big') == 2049)
n <- readBin(f, 'integer', 1L, endian='big')
labels10 <- as.integer(readBin(f, 'raw', n, endian='big'))
close(f)

f <- file('t10k-images-idx3-ubyte', 'rb')
stopifnot(readBin(f, 'integer', 1L, endian='big') == 2051)
stopifnot(readBin(f, 'integer', 1L, endian='big') == n)
nr <- readBin(f, 'integer', 1L, endian='big')
nc <- readBin(f, 'integer', 1L, endian='big')
images10 <- matrix(as.integer(readBin(f, 'raw', n*nr*nc, endian='big')), ncol=nr*nc, byrow=TRUE)
close(f)

f <- file('train-labels-idx1-ubyte', 'rb')
stopifnot(readBin(f, 'integer', 1L, endian='big') == 2049)
n <- readBin(f, 'integer', 1L, endian='big')
labels60 <- as.integer(readBin(f, 'raw', n, endian='big'))
close(f)

f <- file('train-images-idx3-ubyte', 'rb')
stopifnot(readBin(f, 'integer', 1L, endian='big') == 2051)
stopifnot(readBin(f, 'integer', 1L, endian='big') == n)
nr <- readBin(f, 'integer', 1L, endian='big')
nc <- readBin(f, 'integer', 1L, endian='big')
images60 <- matrix(as.integer(readBin(f, 'raw', n*nr*nc, endian='big')), ncol=nr*nc, byrow=TRUE)
close(f)

images <- rbind(images60, images10)

labels <- c(labels60, labels10)
labels[labels==0] <- 10
stopifnot(range(labels)==c(1,10))

f <- gzfile("output.data.gz", open="w")
write.table(images, f, col.names=FALSE, row.names=FALSE, sep=" ", quote=FALSE)
close(f)

f <- gzfile("output.labels0.gz", open="w")
write.table(labels, f, col.names=FALSE, row.names=FALSE, sep=" ", quote=FALSE)
close(f)
