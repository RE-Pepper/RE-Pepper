#pragma once

namespace al
{

class ByamlIter;

class CameraRotatorParam
{
private:
        float mAngleMax;

public:
        void init( const ByamlIter* ticket );

public:
        CameraRotatorParam();
};

} // namespace al
