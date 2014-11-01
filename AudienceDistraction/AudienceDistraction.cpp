// AudienceDistraction.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <opencv\cv.h>      // include it to used Main OpenCV functions.
#include <opencv\highgui.h> //include it to use GUI functions.

int main(int argc, char** argv)
{
	IplImage* img = cvLoadImage("c:/image.jpg"); //change the name (image.jpg) according to your Image filename.
	cvNamedWindow("Example1", CV_WINDOW_AUTOSIZE);
	cvShowImage("Example1", img);
	cvWaitKey(0);
	cvReleaseImage(&img);
	cvDestroyWindow("Example1");
	return 0;
}


