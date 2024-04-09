﻿// Copyright (c) Microsoft Corporation. All rights reserved.
// ChatMessage.cs

using System.Collections.Generic;
using System.Text.Json.Serialization;

namespace AutoGen.Mistral;

public class ChatMessage
{
    /// <summary>
    /// Initializes a new instance of the <see cref="ChatMessage" /> class.
    /// </summary>
    /// <param name="role">role.</param>
    /// <param name="content">content.</param>
    public ChatMessage(RoleEnum? role = default(RoleEnum?), string? content = null)
    {
        this.Role = role;
        this.Content = content;
    }

    [JsonConverter(typeof(JsonPropertyNameEnumConverter<RoleEnum>))]
    public enum RoleEnum
    {
        /// <summary>
        /// Enum System for value: system
        /// </summary>
        [JsonPropertyName("system")]
        //[EnumMember(Value = "system")]
        System = 1,

        /// <summary>
        /// Enum User for value: user
        /// </summary>
        [JsonPropertyName("user")]
        //[EnumMember(Value = "user")]
        User = 2,

        /// <summary>
        /// Enum Assistant for value: assistant
        /// </summary>
        [JsonPropertyName("assistant")]
        //[EnumMember(Value = "assistant")]
        Assistant = 3,

        [JsonPropertyName("tool")]
        Tool = 4,
    }

    /// <summary>
    /// Gets or Sets Role
    /// </summary>
    [JsonPropertyName("role")]
    public RoleEnum? Role { get; set; }

    /// <summary>
    /// Gets or Sets Content
    /// </summary>
    [JsonPropertyName("content")]
    public string? Content { get; set; }

    [JsonPropertyName("tool_calls")]
    public List<FunctionContent>? ToolCalls { get; set; }
}

public class FunctionContent
{
    public FunctionContent(FunctionCall function)
    {
        this.Function = function;
    }

    [JsonPropertyName("function")]
    public FunctionCall Function { get; set; }

    public class FunctionCall
    {
        public FunctionCall(string name, string arguments)
        {
            this.Name = name;
            this.Arguments = arguments;
        }

        [JsonPropertyName("name")]
        public string Name { get; set; }

        [JsonPropertyName("arguments")]
        public string Arguments { get; set; }
    }
}
