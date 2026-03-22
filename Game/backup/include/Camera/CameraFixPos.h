#pragma once

#include <Camera/alCamera.h>

class CameraFixPos : public al::Camera
{
private:
        float _4C;
        float _50;
        float _54;
        float _58;

public:
        virtual void load( const al::ByamlIter* ticket );
        virtual void calc();

public:
        CameraFixPos( const char* name );
};
