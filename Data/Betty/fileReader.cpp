	
	//Set file name and path
	std::string filename = "Betty.raw";

	//Open binary file for reading
	std::ifstream myfile(filename.c_str(), std::ios::in | std::ios::binary);
	if (myfile.is_open()) {

		unsigned char c = 0;
		float f = 0;

		//Loop through data X changes first/fastest.
		for (unsigned int iz = 0; iz < mZMax; iz++)
			for (unsigned int iy = 0; iy < mYMax; iy++)
				for (unsigned int ix = 0; ix < mXMax; ix++) {

					//Initialise empty vector
					my::Vec3f vec = my::Vec3f();

					//Read x then y then z and store in vec (vector)
					//Data needs converting to float from char and adjusted
					myfile.read((char *)&c, 1);
					f = (float)c;
					vec.x = f/255-0.5;

					myfile.read((char *)&c, 1);
					f = (float)c;
					vec.y = f/255-0.5;

					myfile.read((char *)&c, 1);
					f = (float)c;
					vec.z = f/255-0.5;

					//Store vector in datastructure
					mData[iz][iy][ix] = vec;

				}

		//Close the file when finished
		myfile.close();
	}
