local StarterGui = game:GetService("StarterGui")

StarterGui:SetCore("SendNotification", {
	Title = "Scythex is fucked by promax(s)",
	Text = "ez fucked by promax(s) tooo ez",
	Duration = 60,
})

print('SKID EXEC v1.0.3 LOADED')
print('EZ FUCKED BY PROMAX(s)')
printidentity()
print('LV6 HAHA')

local ScreenGui = Instance.new("ScreenGui")
local Frame = Instance.new("Frame")
local Title = Instance.new("TextLabel")
local UIGradient = Instance.new("UIGradient")
local UICorner = Instance.new("UICorner")
local Description = Instance.new("TextLabel")
local UIGradient_2 = Instance.new("UIGradient")
local Close = Instance.new("TextButton")
local UIGradient_3 = Instance.new("UIGradient")
local UICorner_2 = Instance.new("UICorner")

local UIS = game:GetService('UserInputService')
local dragToggle = nil
local dragSpeed = 0.25
local dragStart = nil
local startPos = nil

ScreenGui.Parent = game.Players.LocalPlayer:WaitForChild("PlayerGui")
ScreenGui.ZIndexBehavior = Enum.ZIndexBehavior.Sibling

Frame.Parent = ScreenGui
Frame.BackgroundColor3 = Color3.fromRGB(20, 20, 20)
Frame.BackgroundTransparency = 0.200
Frame.BorderColor3 = Color3.fromRGB(0, 0, 0)
Frame.BorderSizePixel = 0
Frame.ClipsDescendants = true
Frame.Position = UDim2.new(0.410129994, 342, 0.346625775, -175)
Frame.Size = UDim2.new(0.207792208, 0, 0.30674848, 0)
Frame.ZIndex = -2147483648

Title.Name = "Title"
Title.Parent = Frame
Title.BackgroundColor3 = Color3.fromRGB(0, 0, 0)
Title.BackgroundTransparency = 1.000
Title.BorderColor3 = Color3.fromRGB(0, 0, 0)
Title.BorderSizePixel = 0
Title.Position = UDim2.new(0.0199999996, 0, 0, 0)
Title.Size = UDim2.new(0.964999974, 0, 0.166666672, 0)
Title.Font = Enum.Font.Code
Title.Text = "skid exec loaded"
Title.TextColor3 = Color3.fromRGB(255, 255, 255)
Title.TextScaled = true
Title.TextSize = 14.000
Title.TextWrapped = true

UIGradient.Color = ColorSequence.new{ColorSequenceKeypoint.new(0.00, Color3.fromRGB(255, 85, 0)), ColorSequenceKeypoint.new(1.00, Color3.fromRGB(0, 255, 255))}
UIGradient.Parent = Title

UICorner.CornerRadius = UDim.new(0, 20)
UICorner.Parent = Frame

Description.Name = "Description"
Description.Parent = Frame
Description.BackgroundColor3 = Color3.fromRGB(0, 0, 0)
Description.BackgroundTransparency = 1.000
Description.BorderColor3 = Color3.fromRGB(0, 0, 0)
Description.BorderSizePixel = 0
Description.Position = UDim2.new(0.0199999996, 0, 0.196666673, 0)
Description.Size = UDim2.new(0.964999974, 0, 0.636666656, 0)
Description.Font = Enum.Font.Ubuntu
Description.Text = "ez fucked by promax(s)\niHecker pro max & みたらし pro max\nhave fun.\n++ ty to muuchan for support++"
Description.TextColor3 = Color3.fromRGB(255, 255, 255)
Description.TextSize = 20.000
Description.TextWrapped = true
Description.TextXAlignment = Enum.TextXAlignment.Left
Description.TextYAlignment = Enum.TextYAlignment.Top

UIGradient_2.Color = ColorSequence.new{ColorSequenceKeypoint.new(0.00, Color3.fromRGB(255, 85, 0)), ColorSequenceKeypoint.new(1.00, Color3.fromRGB(0, 255, 255))}
UIGradient_2.Parent = Description

Close.Name = "Close"
Close.Parent = Frame
Close.BackgroundColor3 = Color3.fromRGB(255, 120, 120)
Close.BackgroundTransparency = 0.600
Close.BorderColor3 = Color3.fromRGB(0, 0, 0)
Close.Position = UDim2.new(0.0199999996, 0, 0.833333313, 0)
Close.Size = UDim2.new(0.964999974, 0, 0.166666672, 0)
Close.Font = Enum.Font.Ubuntu
Close.Text = "Close"
Close.TextColor3 = Color3.fromRGB(255, 255, 255)
Close.TextSize = 30.000

UIGradient_3.Color = ColorSequence.new{ColorSequenceKeypoint.new(0.00, Color3.fromRGB(255, 85, 0)), ColorSequenceKeypoint.new(1.00, Color3.fromRGB(0, 255, 255))}
UIGradient_3.Parent = Close

UICorner_2.CornerRadius = UDim.new(0, 20)
UICorner_2.Parent = Close

Close.Activated:Connect(function()
	Frame.Visible = false
end)

local function updateInput(input)

	local delta = input.Position - dragStart

	local position = UDim2.new(startPos.X.Scale, startPos.X.Offset + delta.X,

		startPos.Y.Scale, startPos.Y.Offset + delta.Y)

	game:GetService('TweenService'):Create(Frame, TweenInfo.new(dragSpeed), {Position = position}):Play()

end



Frame.InputBegan:Connect(function(input)

	if (input.UserInputType == Enum.UserInputType.MouseButton1 or input.UserInputType == Enum.UserInputType.Touch) then 

		dragToggle = true

		dragStart = input.Position

		startPos = Frame.Position

		input.Changed:Connect(function()

			if input.UserInputState == Enum.UserInputState.End then

				dragToggle = false

			end

		end)

	end

end)



UIS.InputChanged:Connect(function(input)

	if input.UserInputType == Enum.UserInputType.MouseMovement or input.UserInputType == Enum.UserInputType.Touch then

		if dragToggle then

			updateInput(input)

		end

	end

end)

while true do
	wait(0.1)
	local plrGui = game.Players.LocalPlayer:WaitForChild("PlayerGui")
	
	if not plrGui:FindFirstChild("dummtjjjjj") then
		if Frame.Visible == true then
			UIS.MouseIconEnabled = true

			local screengui = Instance.new("ScreenGui", plrGui)
			screengui.Name = "dummtjjjjj"

			local txtButton = Instance.new("TextButton")
			txtButton.BackgroundTransparency = 1
			txtButton.Size = UDim2.new(0, 0, 0, 0)

			txtButton.Modal = true

			txtButton.Parent = screengui
		else
			UIS.MouseIconEnabled = false

			if plrGui:FindFirstChild("dummtjjjjj") then
				print("[EZ FUCKED BY PROMAX(s)] gui destroy'd")
				plrGui:FindFirstChild("dummtjjjjj"):Destroy()
			end
		end
	end
end
