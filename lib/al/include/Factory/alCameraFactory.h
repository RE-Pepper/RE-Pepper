#pragma once

#include <Camera/alCamera.h>
#include <Factory/alFactory.h>

namespace al
{

typedef CreateFuncPtr<Camera>::Type        CreateCameraFuncPtr;
typedef NameToCreator<CreateCameraFuncPtr> NameToCameraCreator;

} // namespace al
