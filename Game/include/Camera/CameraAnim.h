#pragma once

#include <Camera/alCamera.h>

class CameraAnim : public al::Camera
{
private:
        int _4C;
        int _50;
        int _54;
        int _58;

public:
        virtual void load( const al::ByamlIter* ticket );
        virtual void calc();

public:
        CameraAnim( const char* name );
};
