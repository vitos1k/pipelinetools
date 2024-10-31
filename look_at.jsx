pointA = thisLayer;
pointB = thisComp.layer("Null 2");


a = pointA.position[0] - pointB.position[0];
b = pointA.position[1] - pointB.position[1];
switcher = 0;


if (b < 0) {switcher = -180};
if (b == 0) {degree = 90} else {degree = -radiansToDegrees(Math.atan(a/b))}




degree + value + switcher
