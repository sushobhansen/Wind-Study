//Urban 3D symmetric

//Parameters
h = 5.0; //Height of building
w = 5.0; //Width of road = width of building

fetch = 15*h;
wake = 15*h;
lateral = 15*h;
top = 5*h;
lc = 10.0; //Will be overwritten in Transfinite operations
boundaryLayerElements = 4; //Number of refinement cells in BL
cellsInBoundaryLayer = 2; //Number of macro-cells within BL
innerMeshSize = 0.5;
outerMeshSize = innerMeshSize*boundaryLayerElements;
//verticalSize = outerMeshSize/boundaryLayerElements;
verticalSize = 0.5;


//Define points on ground and join them with lines
Point(1) = {0,0,0,lc};
Point(2) = {fetch,0,0,lc};
Point(3) = {fetch+w,0,0,lc};
Point(4) = {fetch+2*w,0,0,lc};
Point(5) = {fetch+3*w,0,0,lc};
Point(6) = {fetch+4*w,0,0,lc};
Point(7) = {fetch+5*w,0,0,lc};
Point(8) = {fetch+5*w+wake,0,0,lc};

Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 5};
Line(5) = {5, 6};
Line(6) = {6, 7};
Line(7) = {7, 8};

Transfinite Line {1} = Ceil(fetch/outerMeshSize) Using Progression 0.9;
Transfinite Line {3,5} = Ceil(w/innerMeshSize) Using Bump 0.25;
Transfinite Line {2:6:2} = Ceil(w/innerMeshSize);
Transfinite Line {7} = Ceil(wake/outerMeshSize) Using Progression 1.1;

Extrude {0,lateral,0}{
	Line{1:7}; Layers{{Ceil((lateral-cellsInBoundaryLayer*innerMeshSize)/outerMeshSize),cellsInBoundaryLayer*boundaryLayerElements},{(lateral-cellsInBoundaryLayer*innerMeshSize)/lateral,1.0}}; Recombine;
}

Extrude {0,w,0}{
	Line{8:32:4}; Layers{Ceil(w/innerMeshSize)}; Recombine;
}

Extrude {0,w,0}{
	Line{36:60:4}; Layers{{cellsInBoundaryLayer*boundaryLayerElements,Ceil((w-2*cellsInBoundaryLayer*innerMeshSize)/innerMeshSize),cellsInBoundaryLayer*boundaryLayerElements},{cellsInBoundaryLayer*innerMeshSize/w,(w-cellsInBoundaryLayer*innerMeshSize)/w,1.0}}; Recombine;
}

Extrude {0,w,0}{
	Line{64:88:4}; Layers{Ceil(w/innerMeshSize)}; Recombine;
}

Extrude {0,w,0}{
	Line{92:116:4}; Layers{{cellsInBoundaryLayer*boundaryLayerElements,Ceil((w-2*cellsInBoundaryLayer*innerMeshSize)/innerMeshSize),cellsInBoundaryLayer*boundaryLayerElements},{cellsInBoundaryLayer*innerMeshSize/w,(w-cellsInBoundaryLayer*innerMeshSize)/w,1.0}}; Recombine;
}

Extrude {0,w,0}{
	Line{120:144:4}; Layers{Ceil(w/innerMeshSize)}; Recombine;
}

Extrude {0,lateral,0}{
	Line{148:172:4}; Layers{{cellsInBoundaryLayer*boundaryLayerElements,Ceil((lateral-cellsInBoundaryLayer*outerMeshSize)/outerMeshSize)},{cellsInBoundaryLayer*innerMeshSize/lateral,1.0}}; Recombine;
}

Extrude {0,0,h}{
	Surface{11:203:4}; Layers{{cellsInBoundaryLayer*boundaryLayerElements,Ceil((h-cellsInBoundaryLayer*verticalSize)/verticalSize)},{cellsInBoundaryLayer*verticalSize/h,1.0}}; Recombine;
}

Transfinite Surface{401:489:44,709:797:44,1017:1105:44}; Recombine Surface "*";

Extrude {0,0,top}{
	Surface{225:1281:22}; Layers{{cellsInBoundaryLayer*boundaryLayerElements,Ceil((top-cellsInBoundaryLayer*verticalSize)/verticalSize)},{cellsInBoundaryLayer*verticalSize/top,1.0}}; Recombine;
}

Recursive Delete{
	Volume{9,11,13,23,25,27,37,39,41};
}

Physical Surface("west") = {1148, 2226, 994, 2072, 840, 1918, 686, 1764, 532, 1610, 378, 1456, 1302, 224};
Physical Surface("south") = {1290, 212, 234, 1312, 256, 1334, 278, 1356, 300, 1378, 322, 1400, 344, 1422};
Physical Surface("east") = {348, 1426, 502, 1580, 656, 1734, 810, 1888, 964, 2042, 1118, 2196, 1272, 2350};
Physical Surface("north") = {2354, 1276, 1254, 2332, 1232, 2310, 2288, 1188, 2266, 1166, 1210, 2244, 1144, 2222};
Physical Surface("atmosphere") = {2227, 2249, 2293, 2315, 2337, 2359, 2271, 2073, 2095, 2117, 2139, 2161, 2183, 2205, 1919, 1941, 1963, 1985, 2029, 2007, 2051, 1765, 1787, 1809, 1831, 1853, 1897, 1875, 1611, 1633, 1655, 1677, 1699, 1721, 1743, 1457, 1479, 1501, 1523, 1545, 1567, 1589, 1303, 1325, 1369, 1347, 1391, 1413, 1435};
Physical Surface("roads1") = {11, 15, 19, 23, 27, 31, 35, 39, 67, 95, 123, 151, 179, 183, 187, 195, 191, 199, 203, 63, 91, 119, 147, 175};
Physical Surface("roads2") = {71, 75, 79, 83, 87, 127, 131, 135, 139, 143};
Physical Surface("roads3") = {159, 167, 103, 111, 47, 55};
Physical Surface("roofs") = {401, 445, 489, 709, 753, 797, 1061, 1105, 1017};
Physical Surface("walls") = {242, 370, 396, 392, 414, 286, 440, 436, 484, 458, 330, 480, 678, 704, 700, 550, 722, 748, 744, 594, 766, 792, 788, 638, 986, 1012, 1008, 858, 1030, 1056, 1052, 902, 946, 1074, 1100, 1096};
Physical Volume("internal") = Volume "*";
